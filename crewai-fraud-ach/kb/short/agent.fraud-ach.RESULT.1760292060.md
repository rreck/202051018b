```json
{
  "id": "7869924875c83b9c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292060,
  "host_pid": "9e6742732c60:1",
  "hash": "ce5cd407019d8a27af162ed1528cc82add354c449348386fd2cf9dff7ebd0a3f",
  "cid": "QmV1ce5cd407019d8a27af162ed1528cc82add354c44",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292060,
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
      "evaluated_at": 1760292060
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
  "sig": "ae0e875e0bbbfffcd5bfe9a72dcdffbb074c5c37c03991a05fea2d6711d719a3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240751710
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 189, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 188, 'first_seen': 1760285763, 'matching_hash': 'c9609c1b2bce9c12'}}}een': 1760284979, 'matching_hash': '445784114b53d57b'}}}