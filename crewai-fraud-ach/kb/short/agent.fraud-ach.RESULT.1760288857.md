```json
{
  "id": "3736972e055bcc35",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288857,
  "host_pid": "9e6742732c60:1",
  "hash": "960905b11b05898607c8d21b37bef82c58bc6b39e701b78a619cc96640db846a",
  "cid": "QmV1960905b11b05898607c8d21b37bef82c58bc6b39",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288857,
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
      "evaluated_at": 1760288857
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
  "sig": "eff9ac19d53c1f2a0ba9ecc67dad6ee96c58e53d9b488ddc95cbe14476f209ad"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597950940
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 106, 'threshold': 50, 'total_amount': 28240202, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 105, 'first_seen': 1760285763, 'matching_hash': 'cd3d42208c2780a3'}}}