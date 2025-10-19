```json
{
  "id": "0e95a27dbba7d6e5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293460,
  "host_pid": "9e6742732c60:1",
  "hash": "908278460e72c835eac22660f0f1c433049e335fa309d10849a7de4849e94764",
  "cid": "QmV1908278460e72c835eac22660f0f1c433049e335f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293460,
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
      "evaluated_at": 1760293460
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
  "sig": "c3a382b6067489e5e46e5499f14be60738f61a037dbc73ecbcd499c3513eb2a4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031117260
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 18094875, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760285763, 'matching_hash': '467ec1c9bc787c3f'}}}