```json
{
  "id": "f207b8c0fdff4542",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291863,
  "host_pid": "9e6742732c60:1",
  "hash": "93b69e4d93d0ab817ad22df8b56b979038ce8c4c8e94c6dea1093b273a67e349",
  "cid": "QmV193b69e4d93d0ab817ad22df8b56b979038ce8c4c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291863,
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
      "evaluated_at": 1760291863
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
  "sig": "22486bd98478dd2708c8829c55f68a95fb08849afc357e784564a7e7de416cb3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034886670
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 185, 'threshold': 50, 'total_amount': 25312625, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 184, 'first_seen': 1760285763, 'matching_hash': 'cbf6d0e6528ee173'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '701651308', 'validation_error': 'Invalid routing number checksum'}}}