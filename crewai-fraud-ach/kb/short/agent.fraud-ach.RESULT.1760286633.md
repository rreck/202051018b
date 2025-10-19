```json
{
  "id": "9aca12683b47049c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286633,
  "host_pid": "9e6742732c60:1",
  "hash": "86436823097b5be91712f7e6ea482a77206b3aa42e0f84d5a44fa1258acd7d52",
  "cid": "QmV186436823097b5be91712f7e6ea482a77206b3aa4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286633,
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
      "evaluated_at": 1760286633
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "0e4728721b1e8a4a22aa815fc44c0a65a503b9f4e97d04707fbe19e5be074d72"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009595856880
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10006176, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 31, 'first_seen': 1760285763, 'matching_hash': '3e252270c9e333bc'}}}round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}routing number checksum'}}}