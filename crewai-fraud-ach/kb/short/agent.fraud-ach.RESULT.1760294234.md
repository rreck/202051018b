```json
{
  "id": "30e6640984a53a76",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294234,
  "host_pid": "9e6742732c60:1",
  "hash": "0355477ecf835ee4b9f1df99a10ac89c16bb2011684c20c6836f7977156a09c2",
  "cid": "QmV10355477ecf835ee4b9f1df99a10ac89c16bb2011",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294234,
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
      "evaluated_at": 1760294234
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
  "sig": "32a29e51fd2a54e65d930b724a3e7654a0553c7c3275bd0f61e33a4c15e864db"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032365153
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 92756430, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285764, 'matching_hash': 'db9686895aceb522'}}}