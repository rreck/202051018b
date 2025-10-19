```json
{
  "id": "4ab7b2ac3bfedcb0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290752,
  "host_pid": "9e6742732c60:1",
  "hash": "d0ec1d614162b726629778ed8e87ce70a45e1e3828fbe8fd318a0324d0203583",
  "cid": "QmV1d0ec1d614162b726629778ed8e87ce70a45e1e38",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290752,
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
      "evaluated_at": 1760290752
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
  "sig": "b41133c8d3645c7825a481ec914a2a72a552df3a78b326442478d5744f3ac0b8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594283807
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 158, 'threshold': 50, 'total_amount': 31848218, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 157, 'first_seen': 1760285764, 'matching_hash': 'e41bbca7fc0ba663'}}}