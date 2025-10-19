```json
{
  "id": "1b68b79781e48e94",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294926,
  "host_pid": "9e6742732c60:1",
  "hash": "df96449f63d968f1b36f5258531314aba49bf0c79ae11f2387739ac1963051bb",
  "cid": "QmV1df96449f63d968f1b36f5258531314aba49bf0c7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294926,
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
      "evaluated_at": 1760294926
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
  "sig": "0bb695b9d277ce7cf9956faf8d4d0259ec7476b2c923a12fdbf0481cc67a2e9a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024745112
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 247, 'threshold': 50, 'total_amount': 14658709, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 246, 'first_seen': 1760285763, 'matching_hash': 'ff21c04b95925b18'}}}