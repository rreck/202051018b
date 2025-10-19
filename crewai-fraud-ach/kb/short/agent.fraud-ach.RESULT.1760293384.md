```json
{
  "id": "4c05aef1ddf3eee8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293384,
  "host_pid": "9e6742732c60:1",
  "hash": "7f04922f42d27148d458a737b7148ba8223cf11327836b11c66fed3dc62a1324",
  "cid": "QmV17f04922f42d27148d458a737b7148ba8223cf113",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293384,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760293384
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "67b86e4ee6ba7810d5b53190dfcca8ca8af9195310642d9d09e897da7011dfe3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468417432
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 73716636, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285764, 'matching_hash': '3485380f8c896007'}}}