```json
{
  "id": "8820599824e98976",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291913,
  "host_pid": "9e6742732c60:1",
  "hash": "40ce7a2e94073e71f5434d0a2d076c653dab2dcc023bbfef6fca49852a088776",
  "cid": "QmV140ce7a2e94073e71f5434d0a2d076c653dab2dcc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291913,
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
      "evaluated_at": 1760291914
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
  "sig": "52b036f77a7c90c3d5fa23f277479253829ec20cf5cb0951b4ed0953c4c7fe46"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 069024451692491
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 186, 'threshold': 50, 'total_amount': 39602934, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 185, 'first_seen': 1760285763, 'matching_hash': '560f842b4bd5b95e'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '069024457', 'validation_error': 'Invalid routing number checksum'}}}