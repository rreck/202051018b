```json
{
  "id": "bfde523e0a61a30d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294408,
  "host_pid": "9e6742732c60:1",
  "hash": "2c4522e203f51563ab91074d4ec9aa02f1b936ef476fe77a46259b32cd9ac909",
  "cid": "QmV12c4522e203f51563ab91074d4ec9aa02f1b936ef",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294408,
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
      "evaluated_at": 1760294408
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
  "sig": "01d4852aeef3389c967a4ea62717dfcef2538c595c35b263e0dce3681664f155"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 735962402542057
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 105121350, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285764, 'matching_hash': '8fcdc870d029f888'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '735962404', 'validation_error': 'Invalid routing number checksum'}}}