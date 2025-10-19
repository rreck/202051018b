```json
{
  "id": "48fb8c162548b618",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292825,
  "host_pid": "9e6742732c60:1",
  "hash": "856b547adcc55f8642df3a4d93a51976f5e898344a92cc5284922825bd41bef5",
  "cid": "QmV1856b547adcc55f8642df3a4d93a51976f5e89834",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292825,
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
      "evaluated_at": 1760292825
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
  "sig": "3924b96f98b98a92f07e4ae68b52df3af322099c192b7241fd97934ff0f9cd1f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277570300
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 83321438, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285763, 'matching_hash': '94740eaab516570d'}}}