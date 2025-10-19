```json
{
  "id": "3f92db9cef1b0284",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291521,
  "host_pid": "9e6742732c60:1",
  "hash": "6ec3e6f4203c8ac9b9bf6641e2cd142922a3795c08ed1b7ba83e0243ba55cf68",
  "cid": "QmV16ec3e6f4203c8ac9b9bf6641e2cd142922a3795c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291521,
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
      "evaluated_at": 1760291521
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
  "sig": "9c4a236fb7f5c10ac917c67a846a1e3009aa09f936ef7c41696a19c0fbdc5185"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460204606
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 177, 'threshold': 50, 'total_amount': 23634279, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 176, 'first_seen': 1760285763, 'matching_hash': 'ff63dbf095b2d177'}}}