```json
{
  "id": "71dfb8caff0991a1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294097,
  "host_pid": "9e6742732c60:1",
  "hash": "12012337e8ec0aae5b899b6b1445da7ed5051116326126e2a10055272517f621",
  "cid": "QmV112012337e8ec0aae5b899b6b1445da7ed5051116",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294097,
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
      "evaluated_at": 1760294097
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
  "sig": "d277ab3c7b063e4886d620cddc35c5a29aa069a55e1a593253439f3f24971d4e"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 107455396447712
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 114843498, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285765, 'matching_hash': 'bb26c320d6c9a382'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '107455391', 'validation_error': 'Invalid routing number checksum'}}}