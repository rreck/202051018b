```json
{
  "id": "408585c9bbe2a833",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287868,
  "host_pid": "9e6742732c60:1",
  "hash": "7b461c112a499406b77fbbde379cf15a5e284e667472f2ea06ed7d7774326caa",
  "cid": "QmV17b461c112a499406b77fbbde379cf15a5e284e66",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287868,
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
      "evaluated_at": 1760287868
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
  "sig": "36936e0d8562ac939548ed03f9d8a94f41a7a662fa37dd8a01da4d499e1a1514"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464168260
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 75, 'threshold': 50, 'total_amount': 11402850, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 74, 'first_seen': 1760285764, 'matching_hash': '4363f5d3ce380aeb'}}}