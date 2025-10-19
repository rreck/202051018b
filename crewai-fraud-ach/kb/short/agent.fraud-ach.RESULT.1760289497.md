```json
{
  "id": "d4b3219d558fc94c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289497,
  "host_pid": "9e6742732c60:1",
  "hash": "621ff5cd48bee54d96d35674b2b277988b993a19cd660844d38790d3bf68ad79",
  "cid": "QmV1621ff5cd48bee54d96d35674b2b277988b993a19",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289497,
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
      "evaluated_at": 1760289497
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
  "sig": "85b482b82507a18013ab60de17485e1daf60d49a272c4972921c20238d38270c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029921508
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 125, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 124, 'first_seen': 1760285763, 'matching_hash': 'c334adb3999837f9'}}}