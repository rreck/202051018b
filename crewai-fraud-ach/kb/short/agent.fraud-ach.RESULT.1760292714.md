```json
{
  "id": "ae4169a39869259e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292714,
  "host_pid": "9e6742732c60:1",
  "hash": "3c2e21cb6560a39fb0cc12928728bda7e5f425c067fd0770cf8d48e0f78b0ecd",
  "cid": "QmV13c2e21cb6560a39fb0cc12928728bda7e5f425c0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292714,
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
      "evaluated_at": 1760292714
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
  "sig": "57d50d210ab11d1ba12b634cbf9443a085208331c6cf60188961ce202e9e381e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155194168
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 74225935, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285765, 'matching_hash': '7ab74b64ae25594e'}}}