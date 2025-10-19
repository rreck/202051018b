```json
{
  "id": "235ed031bd31b9d2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293419,
  "host_pid": "9e6742732c60:1",
  "hash": "1b6294d96fd026713b5c87d01837584b55627cbb7bc6b5c530506cb75049c980",
  "cid": "QmV11b6294d96fd026713b5c87d01837584b55627cbb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293419,
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
      "evaluated_at": 1760293419
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
  "sig": "e5a785fe6a84f86866e41bd14e0fbfb056fa0dce10a391da6d06e09a6e6ee09d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598880520
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 41521152, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760285764, 'matching_hash': '9fe1b03994749115'}}}