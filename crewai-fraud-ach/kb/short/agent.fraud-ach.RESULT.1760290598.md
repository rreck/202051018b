```json
{
  "id": "2324e8f27e3856c6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290598,
  "host_pid": "9e6742732c60:1",
  "hash": "75165be3fefc793b294bcf7147455b581865e42fd48353b8925b502d422948ff",
  "cid": "QmV175165be3fefc793b294bcf7147455b581865e42f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290598,
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
      "evaluated_at": 1760290598
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
  "sig": "8fd86e7cd6fa10fe4600dc9192f2873f35ba7e9ee224c89a67680d1600f3cae5"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 272809904666410
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 154, 'threshold': 50, 'total_amount': 47884144, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 153, 'first_seen': 1760285765, 'matching_hash': 'b8be43189937b834'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '272809901', 'validation_error': 'Invalid routing number checksum'}}}