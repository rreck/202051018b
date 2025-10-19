```json
{
  "id": "1b1f30fe6438701a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293837,
  "host_pid": "9e6742732c60:1",
  "hash": "a90caa9b5b4167d140440936360c2d5e240f5128bfc8860150e1741880e2f1f8",
  "cid": "QmV1a90caa9b5b4167d140440936360c2d5e240f5128",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293837,
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
      "evaluated_at": 1760293837
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
  "sig": "45c072efa9b7a84c0c08e9e641f4c93d538fa5955a293be4ba4cf53500f688fe"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155194168
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 82635770, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285765, 'matching_hash': '7ab74b64ae25594e'}}}