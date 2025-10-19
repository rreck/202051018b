```json
{
  "id": "2d8c0b8289a407cf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288766,
  "host_pid": "9e6742732c60:1",
  "hash": "eeeda41cc0955c3808b5c64ce2a5fd8699804cffc7372b73e20bfd39634a40c0",
  "cid": "QmV1eeeda41cc0955c3808b5c64ce2a5fd8699804cff",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288766,
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
      "evaluated_at": 1760288766
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
  "sig": "bb4882fb7de49bb10e88f780d0ebd7a025d4f914e152dd64d5fde95ae714d247"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464250877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 103, 'threshold': 50, 'total_amount': 38416837, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 102, 'first_seen': 1760285765, 'matching_hash': '9a278d14d50dbff1'}}}