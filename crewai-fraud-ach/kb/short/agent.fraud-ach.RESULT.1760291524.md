```json
{
  "id": "de303e387f0ef610",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291524,
  "host_pid": "9e6742732c60:1",
  "hash": "511904de37a9f3dd83d545f00a26eeb8b685c57c5152f44c52ae8252fcd4bb1d",
  "cid": "QmV1511904de37a9f3dd83d545f00a26eeb8b685c57c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291524,
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
      "evaluated_at": 1760291524
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
  "sig": "28347518d0f5e72070f20f55299f02f6ab5abfa725cedfa9c801a7d2da199327"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244248906
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 177, 'threshold': 50, 'total_amount': 24771681, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 176, 'first_seen': 1760285764, 'matching_hash': '29854d353b99a4c0'}}}