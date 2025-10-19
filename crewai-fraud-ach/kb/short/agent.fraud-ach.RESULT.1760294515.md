```json
{
  "id": "4199e608c6a3dc19",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294515,
  "host_pid": "9e6742732c60:1",
  "hash": "b77b6211b7864ff3071fc56112e5feb248543ef36eb8855da772c60836e07e65",
  "cid": "QmV1b77b6211b7864ff3071fc56112e5feb248543ef3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294515,
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
      "evaluated_at": 1760294515
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
  "sig": "9bcb335af7d61012d1baad05d6d5224333f207e1d549054c875f14e1e061378e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152430853
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 20144593, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285764, 'matching_hash': 'fa17beca2cfad33c'}}}