```json
{
  "id": "8f7e6be2080c4f3d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288725,
  "host_pid": "9e6742732c60:1",
  "hash": "d4ebde8a68e2aaa61c91e72a140b0e281cfa94f8c41b8b0481ef54d7d2512fab",
  "cid": "QmV1d4ebde8a68e2aaa61c91e72a140b0e281cfa94f8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288725,
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
      "evaluated_at": 1760288725
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
  "sig": "487f60c295ee3edf633afe59bf01a6608004c3aa02d920bb2f58943384d66ee8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035410213
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 102, 'threshold': 50, 'total_amount': 39267042, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 101, 'first_seen': 1760285763, 'matching_hash': '3fae4375ff781af3'}}}