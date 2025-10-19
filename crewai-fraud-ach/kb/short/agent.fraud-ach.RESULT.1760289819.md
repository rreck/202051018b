```json
{
  "id": "9dc2d4d6405d8cee",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289819,
  "host_pid": "9e6742732c60:1",
  "hash": "d0c1c48eb82fa3170614ef7354f30f9f324468cdea514cbf3721d3663edbf280",
  "cid": "QmV1d0c1c48eb82fa3170614ef7354f30f9f324468cd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289819,
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
      "evaluated_at": 1760289819
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
  "sig": "3dd30284183a1dea23b311efe72fedc08179ee8abde13e35dce2adb7b2f5dcb9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029536226
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 134, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 133, 'first_seen': 1760285763, 'matching_hash': 'ee8686fc8d545b2d'}}}een': 1760285763, 'matching_hash': '9b2dabf2ca05df4f'}}}