```json
{
  "id": "aa2d361c0ed68206",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290306,
  "host_pid": "9e6742732c60:1",
  "hash": "0ab60d7aedf9c776aca73df572dbdeeb44e0670922d94bc6848de5bf6d8a37c8",
  "cid": "QmV10ab60d7aedf9c776aca73df572dbdeeb44e06709",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290306,
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
      "evaluated_at": 1760290306
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
  "sig": "2ba67c59f3c9c55581caa4d2ca750acd85ee4a7e289f44c7cdc89efcf0478b7a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028270724
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 147, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 146, 'first_seen': 1760285763, 'matching_hash': 'c4ee7f0f971d402b'}}}een': 1760285763, 'matching_hash': 'ff63dbf095b2d177'}}}