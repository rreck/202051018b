```json
{
  "id": "e2578231ed417fbf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285289,
  "host_pid": "9e6742732c60:1",
  "hash": "709fbbb82e2bdfaa1f8e49c138d1a55f90dc3bd13d5fe5c422fd0f4cbb84ff2b",
  "cid": "QmV1709fbbb82e2bdfaa1f8e49c138d1a55f90dc3bd1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285289,
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
      "evaluated_at": 1760285289
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
  "sig": "1ff536874cf903d48860af8df11fe6a5b94aa7ac2bd4abfb7eef423ad29fd18d"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105154887163
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10905769, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 30, 'first_seen': 1760284979, 'matching_hash': '445784114b53d57b'}}}