```json
{
  "id": "46ec864663cb9d70",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292801,
  "host_pid": "9e6742732c60:1",
  "hash": "f49ade232506b40a08aed9e682aea784a9b311740d3e05d6b0935bedb58f02cf",
  "cid": "QmV1f49ade232506b40a08aed9e682aea784a9b31174",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292801,
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
      "evaluated_at": 1760292801
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
  "sig": "8392e32898ad7789ac84d173ef86e1c2301e9112f89e6a3dffdfaeb6de64b9d3"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 288759219871928
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 87608595, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760285763, 'matching_hash': '2df17da091128ee2'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '288759214', 'validation_error': 'Invalid routing number checksum'}}}