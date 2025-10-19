```json
{
  "id": "eb530cf1f4cb8c21",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285894,
  "host_pid": "9e6742732c60:1",
  "hash": "460b3e6fabbd160b53f0036a0653292241433382b1abfb24b77ca787225111c9",
  "cid": "QmV1460b3e6fabbd160b53f0036a0653292241433382",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285894,
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
      "evaluated_at": 1760285894
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
  "sig": "07a776a35a86d46f04cb735382ecad247199b4c3c6c235b61eda32169209cf70"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000243177921
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 6, 'first_seen': 1760285765, 'matching_hash': '2e3fb8f97f4f3efd'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}