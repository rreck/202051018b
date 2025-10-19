```json
{
  "id": "c2f8090563171cba",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291910,
  "host_pid": "9e6742732c60:1",
  "hash": "d0821ff6293da3b5dc3abd60de233290e957500c5ddb99a19db67cc96fd01337",
  "cid": "QmV1d0821ff6293da3b5dc3abd60de233290e957500c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291910,
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
      "evaluated_at": 1760291910
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
  "sig": "937b5e476d97c181f14ce53271edf1c124ee4b149a35140cb741de4d481884f4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153452209
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 186, 'threshold': 50, 'total_amount': 58624596, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 185, 'first_seen': 1760285763, 'matching_hash': 'ba46400915da6233'}}}