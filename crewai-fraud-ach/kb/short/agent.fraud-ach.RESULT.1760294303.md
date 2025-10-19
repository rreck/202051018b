```json
{
  "id": "8470ed602de09b05",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294303,
  "host_pid": "9e6742732c60:1",
  "hash": "20bb92338ed5349c2ec2ea4d76b8a1eda6f41bec16c1e40904adbd7af67ca801",
  "cid": "QmV120bb92338ed5349c2ec2ea4d76b8a1eda6f41bec",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294303,
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
      "evaluated_at": 1760294303
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
  "sig": "604a3503dd9f3cf7c7e54004ab1b430dceb8b93862189ddb7c83a388d17ee141"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464250877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 87650065, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285765, 'matching_hash': '9a278d14d50dbff1'}}}