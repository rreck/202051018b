```json
{
  "id": "d8c24b2e61c7c408",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290615,
  "host_pid": "9e6742732c60:1",
  "hash": "2c201ad95b2b69e645f158e53a3ad28c5f951bb9162a4baa903c0c3cb8f987c1",
  "cid": "QmV12c201ad95b2b69e645f158e53a3ad28c5f951bb9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290615,
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
      "evaluated_at": 1760290615
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
  "sig": "3c45c8077bf3333cd0e4919f1fcfa469ad0709ee52f7d6e0aa3f018a7d87f52e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029921508
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 155, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 154, 'first_seen': 1760285763, 'matching_hash': 'c334adb3999837f9'}}}een': 1760285763, 'matching_hash': 'e52038f69d26fe5a'}}}