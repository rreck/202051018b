```json
{
  "id": "a27e5c3dc17b07e9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288650,
  "host_pid": "9e6742732c60:1",
  "hash": "1abe11d110de7bc90eddf79eb328cd61aa8984fb63308360c4b4fcd4fe667e86",
  "cid": "QmV11abe11d110de7bc90eddf79eb328cd61aa8984fb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288650,
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
      "evaluated_at": 1760288650
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
  "sig": "30868d4ee6cdf641aa3793f0e976a562ac1e14d4e18802ef2f8c2b6ca9a06032"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591278492
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 100, 'threshold': 50, 'total_amount': 12472600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 99, 'first_seen': 1760285763, 'matching_hash': '3e8e4f28808ab222'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}