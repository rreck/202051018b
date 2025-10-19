```json
{
  "id": "48c1c103e66bb73a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294513,
  "host_pid": "9e6742732c60:1",
  "hash": "145edf2091ca606c6ca3ae796323d50339b278f7fa51c9483ace01b0de7b1067",
  "cid": "QmV1145edf2091ca606c6ca3ae796323d50339b278f7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294513,
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
      "evaluated_at": 1760294513
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
  "sig": "2fe767ca6dda5f58a9879e61c49389930e3cb6afbeab76ce71c42b32548d743a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105159090424
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 41331943, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285764, 'matching_hash': 'fe78f8ea626833d8'}}}