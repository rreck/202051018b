```json
{
  "id": "4ad292278de25b01",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288015,
  "host_pid": "9e6742732c60:1",
  "hash": "3bee4220a84d9b2f0a86e49e107dd1353af5199e4c587ae96a3faf0fca4ddccb",
  "cid": "QmV13bee4220a84d9b2f0a86e49e107dd1353af5199e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288015,
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
      "evaluated_at": 1760288015
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
  "sig": "58c0ff79fabcb01286f6a72444fffee0d36ba80494c07946485ccd7144c83070"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156237747
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 80, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 79, 'first_seen': 1760285763, 'matching_hash': 'b60e159429465bd2'}}}