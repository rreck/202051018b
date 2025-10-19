```json
{
  "id": "f532600adde820ba",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290637,
  "host_pid": "9e6742732c60:1",
  "hash": "6e17eb5097dae366d81d80412a8b8f24caf25fa3db0780134b9dbad9b47e93a8",
  "cid": "QmV16e17eb5097dae366d81d80412a8b8f24caf25fa3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290637,
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
      "evaluated_at": 1760290637
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
  "sig": "a97ed2a5b2362093418a211bc03512dcdf95768e30a58eadfa0cdaf679c263b1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155194168
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 155, 'threshold': 50, 'total_amount': 56674975, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 154, 'first_seen': 1760285765, 'matching_hash': '7ab74b64ae25594e'}}}