```json
{
  "id": "d700feef54413a9c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294331,
  "host_pid": "9e6742732c60:1",
  "hash": "e9e6cf19818031e2599ba91daa98e7ae566496c82a6adee542749749904ebae0",
  "cid": "QmV1e9e6cf19818031e2599ba91daa98e7ae566496c8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294331,
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
      "evaluated_at": 1760294332
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
  "sig": "f6a52c8de6fa6faa7f3b5656b92d746a9ccff9d45291e661bf7509bd53a3bb2e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242946545
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 39158772, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285763, 'matching_hash': '62b45bc192f4101a'}}}}