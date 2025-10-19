```json
{
  "id": "c751ba1547b66a8f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286730,
  "host_pid": "9e6742732c60:1",
  "hash": "0f722ad3fba3e4feff90ddb0e48926b9ecb826ca52cc05963d01e84fcec6f457",
  "cid": "QmV10f722ad3fba3e4feff90ddb0e48926b9ecb826ca",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286730,
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
      "evaluated_at": 1760286730
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
  "sig": "e85e75527c42c1c8592dd3790561158e01743de9981e870fd69eeaf2df57f4b4"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000024765233
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11937030, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 34, 'first_seen': 1760285763, 'matching_hash': 'feb1cc4bc40c71bc'}}}