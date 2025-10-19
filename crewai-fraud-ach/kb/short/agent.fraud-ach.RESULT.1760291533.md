```json
{
  "id": "008deddab849dec2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291533,
  "host_pid": "9e6742732c60:1",
  "hash": "06be7286927bd5dabe18bf22c603d3fe19e8878f4fb05ebabff3d25aba4c28e5",
  "cid": "QmV106be7286927bd5dabe18bf22c603d3fe19e8878f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291533,
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
      "evaluated_at": 1760291533
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
  "sig": "c1406a0edf0040f4d62beacd18b888010fccc3496b8dd6713ae01d275e6d71c0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468078455
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 177, 'threshold': 50, 'total_amount': 79464681, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 176, 'first_seen': 1760285764, 'matching_hash': '379f6acb9d31a698'}}}