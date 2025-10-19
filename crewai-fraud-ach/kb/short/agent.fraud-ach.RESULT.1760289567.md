```json
{
  "id": "e635158734d8fc20",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289567,
  "host_pid": "9e6742732c60:1",
  "hash": "ae84931904bac04c30d51e1a38caede530e02aee0ec6c0b5e276cea769ade004",
  "cid": "QmV1ae84931904bac04c30d51e1a38caede530e02aee",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289567,
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
      "evaluated_at": 1760289567
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
  "sig": "c7cb462106d7e4a4fece9112fd4aa1caadc5bf54bd39bc77151957fe74702419"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029921508
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 127, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 126, 'first_seen': 1760285763, 'matching_hash': 'c334adb3999837f9'}}}een': 1760285763, 'matching_hash': 'cc2974580ec11a3c'}}}