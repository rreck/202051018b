```json
{
  "id": "d4715eaecf4166ba",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289832,
  "host_pid": "9e6742732c60:1",
  "hash": "f1c44df658af67749947c8f874f33216bea3073063fdcd24c674715e6db6ded0",
  "cid": "QmV1f1c44df658af67749947c8f874f33216bea30730",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289832,
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
      "evaluated_at": 1760289832
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
  "sig": "7af818a94747438f317415382cb3e16cb0f78640f6033e31fcd5542622d044df"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022074928
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 134, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 133, 'first_seen': 1760285765, 'matching_hash': 'a87d8bfbdd334181'}}}een': 1760285763, 'matching_hash': '7890640eadac4bcb'}}}