```json
{
  "id": "364833c9bf875cda",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289461,
  "host_pid": "9e6742732c60:1",
  "hash": "ab3b367b8225dd58400fb7287ccbdabda222e9bde5529fa70e4442bdd3a32bfb",
  "cid": "QmV1ab3b367b8225dd58400fb7287ccbdabda222e9bd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289461,
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
      "evaluated_at": 1760289461
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
  "sig": "ab6a92de02a20585f1ad7a37b5025db176221253bc53880f168b32d5418505f6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469028209
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 124, 'threshold': 50, 'total_amount': 30273236, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 123, 'first_seen': 1760285763, 'matching_hash': 'a4269a968e85dafe'}}}