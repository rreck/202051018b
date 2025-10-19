```json
{
  "id": "90646a20d1d07ab1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291124,
  "host_pid": "9e6742732c60:1",
  "hash": "799c277d5085f53dc26b49d5567fa2e6db9995ed36e324ec002115e09e2aab3f",
  "cid": "QmV1799c277d5085f53dc26b49d5567fa2e6db9995ed",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291124,
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
      "evaluated_at": 1760291124
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
  "sig": "acae7e731b11ecb25727ec052277d12599e19d87bf60d93145e84c976560c760"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 167, 'threshold': 50, 'total_amount': 53147416, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 166, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}