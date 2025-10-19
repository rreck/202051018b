```json
{
  "id": "52ba139757db7249",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292795,
  "host_pid": "9e6742732c60:1",
  "hash": "5da12707903b4422de573f407c5243bc21bdf32e0b1b6c90f482307b18b110b2",
  "cid": "QmV15da12707903b4422de573f407c5243bc21bdf32e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292795,
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
      "evaluated_at": 1760292795
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
  "sig": "a3e2ad73849774b75ebd2af1cebfaed1d79e336b59f1a1e24614692054c38806"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248887344
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 12117345, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760285764, 'matching_hash': '5acb0608ecf9576e'}}}