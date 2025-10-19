```json
{
  "id": "ad2695075f9b9098",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294455,
  "host_pid": "9e6742732c60:1",
  "hash": "f3a7820ffc27e88f360d889dc2ea46c03105be67246fa025bf7497a1e0951c50",
  "cid": "QmV1f3a7820ffc27e88f360d889dc2ea46c03105be67",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294455,
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
      "evaluated_at": 1760294456
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
  "sig": "d1cb52fd0e38793f5f4f7047cd3a0d2ac9629fb6bec6ead9d3a8a9c82e637975"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465836827
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 314, 'threshold': 50, 'total_amount': 65732760, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 313, 'first_seen': 1760284979, 'matching_hash': '8a0ab7f0e4aa4922'}}}