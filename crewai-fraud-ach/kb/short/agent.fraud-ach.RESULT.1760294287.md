```json
{
  "id": "5168c0b95583fd0b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294287,
  "host_pid": "9e6742732c60:1",
  "hash": "9384f12f92dd24b74cb93cc3e3cfed24695ab81f9af6dd39f5b37867ffca5842",
  "cid": "QmV19384f12f92dd24b74cb93cc3e3cfed24695ab81f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294287,
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
      "evaluated_at": 1760294287
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
  "sig": "fd2f85400ce67e83e9b44fa7c9803994fa81dcd8ae001286f9fc03ecc181a147"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277214063
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 67340425, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285763, 'matching_hash': 'ff6f9f90137c8ef9'}}}