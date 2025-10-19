```json
{
  "id": "dabc298fd876edf8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293638,
  "host_pid": "9e6742732c60:1",
  "hash": "e5f520b869f6ee2a92431bd9c6b3e0ae9083e94c687326592a2998649b4caacd",
  "cid": "QmV1e5f520b869f6ee2a92431bd9c6b3e0ae9083e94c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293638,
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
      "evaluated_at": 1760293638
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
  "sig": "c94f2edbe07c97720bf6f053865393c6a09ebdd91cfedbbab47e0a75d5185c22"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020143117
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 55500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285765, 'matching_hash': '83c798d1c8d9cfec'}}}