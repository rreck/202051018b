```json
{
  "id": "99e0464069b8ef7a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289615,
  "host_pid": "9e6742732c60:1",
  "hash": "49e5009d9cc5db45563ff13dd7e3e54869787ee7a89986bc2e94214747590a22",
  "cid": "QmV149e5009d9cc5db45563ff13dd7e3e54869787ee7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289615,
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
      "evaluated_at": 1760289615
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
  "sig": "12511b8a40ad82eaaec46537a1cb069ed2388259538486bd39b499a1da0ea30c"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 789209528183836
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 128, 'threshold': 50, 'total_amount': 33375616, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 127, 'first_seen': 1760285765, 'matching_hash': 'e8f44f77b3005867'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '789209527', 'validation_error': 'Invalid routing number checksum'}}}