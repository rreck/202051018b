```json
{
  "id": "259bf6edc45bfed3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287251,
  "host_pid": "9e6742732c60:1",
  "hash": "a88278414f8f971d031baf41fffc06b08e0b91a4d2339dbca8ba80b8f4b2c685",
  "cid": "QmV1a88278414f8f971d031baf41fffc06b08e0b91a4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287251,
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
      "evaluated_at": 1760287251
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "606ebe4e6ad23733d0d4f2b6f3b85945b42acc00ca88364f4b812ce52d7b1c64"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000024542500
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 53, 'threshold': 50, 'total_amount': 22967974, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 52, 'first_seen': 1760285765, 'matching_hash': 'f616428a070fc3ba'}}}