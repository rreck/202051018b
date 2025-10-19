```json
{
  "id": "b1de0f171995fe72",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294072,
  "host_pid": "9e6742732c60:1",
  "hash": "ef67cdf7fbfcffbe22329fd70cb07934a6b5d1bd847180d116a46d276189b8d4",
  "cid": "QmV1ef67cdf7fbfcffbe22329fd70cb07934a6b5d1bd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294072,
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
      "evaluated_at": 1760294072
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
  "sig": "48805be5ddfabb0a3f60c82da756c54324491a0fe0d44033572f468e7011fde0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000021906357
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 101128797, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285764, 'matching_hash': '507361b82f38c481'}}}