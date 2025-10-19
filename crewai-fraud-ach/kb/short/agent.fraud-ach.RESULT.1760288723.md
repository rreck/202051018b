```json
{
  "id": "ae722a7b5fd6b3c4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288723,
  "host_pid": "9e6742732c60:1",
  "hash": "2e2d723c1749013f500f61421e131af1988223828c3aa677939cf5d968fee549",
  "cid": "QmV12e2d723c1749013f500f61421e131af198822382",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288723,
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
      "evaluated_at": 1760288723
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
  "sig": "099a28903b3fc76c05af6452f73161183f8c440436dc0a94c3f0a509e97a2bcd"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 886156735269080
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 102, 'threshold': 50, 'total_amount': 19563702, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 101, 'first_seen': 1760285765, 'matching_hash': 'bf20bb751245cb05'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '886156735', 'validation_error': 'Invalid routing number checksum'}}}