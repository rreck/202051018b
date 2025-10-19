```json
{
  "id": "1594b3324a5de59f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289943,
  "host_pid": "9e6742732c60:1",
  "hash": "f1226d30132642736ad145e27fb5abc388da9c3c56186162df5dad8d54b7a54e",
  "cid": "QmV1f1226d30132642736ad145e27fb5abc388da9c3c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289943,
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
      "evaluated_at": 1760289943
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
  "sig": "acb84c82c5fc846500a839f5d369c53be371dc7a02dbe730f6cb2f3e370ca13a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245772760
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 137, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 136, 'first_seen': 1760285763, 'matching_hash': '6b0c370090b6c980'}}}een': 1760285765, 'matching_hash': 'bcd6f6796bd6b696'}}}