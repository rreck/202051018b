```json
{
  "id": "4434e6edc3251330",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288204,
  "host_pid": "9e6742732c60:1",
  "hash": "b21006e28d543977763b998ec2056f7d700e452e260a1a81a82a55bb742d4aff",
  "cid": "QmV1b21006e28d543977763b998ec2056f7d700e452e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288204,
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
      "evaluated_at": 1760288204
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
  "sig": "2fe0759170d2305260bd076928d1dffae7a5fc33df17040e61633ca0ee8e9ebf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157190044
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 86, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 85, 'first_seen': 1760285763, 'matching_hash': '3b9549cbaaa9aa1e'}}}een': 1760285764, 'matching_hash': '58071665864a5dbb'}}}