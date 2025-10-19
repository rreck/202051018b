```json
{
  "id": "06266b1f37fbe620",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292975,
  "host_pid": "9e6742732c60:1",
  "hash": "e1e91293c409a45cb9cac7b5eecc3d42793cf483bc1d20234e5bc933bcf36729",
  "cid": "QmV1e1e91293c409a45cb9cac7b5eecc3d42793cf483",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292975,
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
      "evaluated_at": 1760292975
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "5e49e0728a32de72e97bfbfa19c5ca59b06b44bf6fa58c76468e03762e2970cb"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 372851334846795
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 102810862, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285763, 'matching_hash': 'e24b6b5408d67f01'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '372851336', 'validation_error': 'Invalid routing number checksum'}}}